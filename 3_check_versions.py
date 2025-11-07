# check_versions.py
import sys
print(f"Python version: {sys.version}")

try:
    import pyspark
    print(f"PySpark version: {pyspark.__version__}")
except ImportError as e:
    print(f"PySpark import error: {e}")

if sys.version_info.major == 3 and sys.version_info.minor == 13:
    print("несовместимость версий (скорее всего)")
else:
    print("✅ Успех!")
