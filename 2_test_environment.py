import os
import sys

def check_environment_variables():
    """Проверяет наличие переменных окружения"""
    
    variables_to_check = ['JAVA_HOME', 'HADOOP_HOME', 'SPARK_HOME']
    
    print("🔍 Проверка переменных окружения Hadoop/Spark")
    print("=" * 50)
    
    results = {}
    
    for var in variables_to_check:
        value = os.getenv(var)
        results[var] = value
        
        status = "✓ НАЙДЕНА" if value else "✗ ОТСУТСТВУЕТ"
        print(f"{var:<15} {status}")
        
        if value:
            print(f"              Путь: {value}")
    
    print("=" * 50)
    
    # Проверяем, все ли переменные найдены
    missing_vars = [var for var, value in results.items() if not value]
    
    if not missing_vars:
        print("✅ Все необходимые переменные настроены!")
        return True
    else:
        print(f"❌ Отсутствуют переменные: {', '.join(missing_vars)}")
        return False

if __name__ == "__main__":
    success = check_environment_variables()
    sys.exit(0 if success else 1)