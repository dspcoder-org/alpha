
import subprocess
import re
from pathlib import Path
from typing import Dict, Optional, List

class ValgrindAnalyzer:
    def __init__(self, executable_path: str, input=None):
        self.executable_path = Path(executable_path)
        if not self.executable_path.is_file():
            raise FileNotFoundError(f"Executable not found: {executable_path}")
        self.args = []
        self.ip = input
        self.__version__ = "0.0.1"

    def get_memory_footprint(self) -> Dict[str, int]:
        """Analyze memory usage using Massif with improved parsing."""
        massif_out = "massif.out"
        cmd = [
            "/dspcoder/valgrind/bin/valgrind",
            "--tool=massif",
            f"--massif-out-file={massif_out}",
            "--detailed-freq=1",
            "--pages-as-heap=yes",
            "--stacks=yes",  # Explicitly track stack
            str(self.executable_path),
            *self.args
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True, input=self.ip)
            
            # Use ms_print to get detailed snapshot info
            ms_print_cmd = ["/dspcoder/valgrind/bin/ms_print", massif_out]
            ms_print_result = subprocess.run(ms_print_cmd, capture_output=True, text=True)
            
            return self._parse_memory_data(ms_print_result.stdout, massif_out)
        finally:
            try:
                Path(massif_out).unlink()
            except Exception:
                pass

    def _parse_memory_data(self, ms_print_output: str, massif_file: str) -> Dict[str, int]:
        """Enhanced parser for memory data."""
        stats = {'heap_usage': 0, 'stack_usage': 0, 'total_ram': 0}
        
        # Parse raw massif file for detailed information
        try:
            with open(massif_file, 'r') as f:
                content = f.read()
                
            # Find peak heap snapshot
            heap_snapshots = re.findall(r'mem_heap_B=(\d+)', content)
            if heap_snapshots:
                stats['heap_usage'] = max(map(int, heap_snapshots))
            
            # Find peak stack snapshot
            stack_snapshots = re.findall(r'mem_stacks_B=(\d+)', content)
            if stack_snapshots:
                stats['stack_usage'] = max(map(int, stack_snapshots))
        except Exception as e:
            print(f"Warning: Error parsing massif file: {e}")

        # Parse ms_print output for additional verification
        peak_match = re.search(r'(?:Peak heap usage:|The peak memory consumption was) (\d+)', ms_print_output)
        if peak_match and not stats['heap_usage']:
            stats['heap_usage'] = int(peak_match.group(1))
            
        # Calculate total RAM
        stats['total_ram'] = stats['heap_usage'] + stats['stack_usage']
        
        return stats

    def check_memory_leaks(self) -> Dict[str, int]:
        """Check memory leaks using Memcheck with improved accuracy."""
        cmd = [
            "/dspcoder/valgrind/bin/valgrind",
            "--tool=memcheck",
            "--leak-check=full",
            "--show-leak-kinds=all",
            "--track-origins=yes",
            "--verbose",  # Add verbose output
            str(self.executable_path),
            *self.args
        ]

        result = subprocess.run(cmd, check=True, capture_output=True, text=True, input=self.ip)
        return self._parse_leak_output(result.stderr)

    def _parse_leak_output(self, output: str) -> Dict[str, int]:
        """Enhanced parser for memory leak output."""
        patterns = {
            'definitely_lost': r'definitely lost: ([0-9,]+) bytes',
            'indirectly_lost': r'indirectly lost: ([0-9,]+) bytes',
            'possibly_lost': r'possibly lost: ([0-9,]+) bytes',
            'still_reachable': r'still reachable: ([0-9,]+) bytes',
            'suppressed': r'suppressed: ([0-9,]+) bytes'
        }
        
        stats = {key: 0 for key in patterns}
        for key, pattern in patterns.items():
            matches = re.finditer(pattern, output, re.IGNORECASE)
            # Sum all occurrences
            for match in matches:
                value = match.group(1).replace(',', '')
                stats[key] += int(value)
                
        return stats

    def get_cache_profile(self) -> Dict[str, int]:
        """Analyze cache usage using Cachegrind with improved accuracy."""
        cmd = [
            "/dspcoder/valgrind/bin/valgrind",
            "--tool=cachegrind",
            "--cachegrind-out-file=cachegrind.out",
            "--branch-sim=yes",  # Enable branch prediction simulation
            "--cache-sim=yes",   # Enable cache simulation
            str(self.executable_path),
            *self.args
        ]

        result = subprocess.run(cmd, check=True, capture_output=True, text=True, input=self.ip)
        return self._parse_cache_output(result.stderr+result.stdout)

    def _parse_cache_output(self, output: str) -> Dict[str, int]:
        """Enhanced parser for cache profiling output."""
        patterns = {
            'l1_miss': r'D1\s+misses:\s+([0-9,]+)',
            'l2_miss': r'L2d\s+misses:\s+([0-9,]+)',
            'branch_miss': r'Branches:\s+([0-9,]+)\s+([0-9,]+)\s+([0-9,.]+)%'
        }
        
        stats = {key: 0 for key in patterns}
        for key, pattern in patterns.items():
            match = re.search(pattern, output, re.IGNORECASE)
            if match:
                if key == 'branch_miss':
                    # For branch misses, use the percentage
                    stats[key] = int(float(match.group(3).replace(',', '')))
                else:
                    stats[key] = int(match.group(1).replace(',', ''))
                    
        return stats



