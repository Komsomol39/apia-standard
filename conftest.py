import sys
from pathlib import Path

# Add repo root to path so 'from cli.apia import ...' works
sys.path.insert(0, str(Path(__file__).parent))
