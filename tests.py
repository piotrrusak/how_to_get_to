import subprocess
import os

# Lista tras (start, end)
test_cases = [
    # ("(21, 115)", "(137, 32)"),
    # ("(10, 96)", "(123, 38)"),
    # ("(49, 119)", "(47, 58)"),
    # ("(90, 111)", "(106, 90)"),
    ("(43, 76)", "(7, 128)"),
    # ("(37, 124)", "(103, 44)"),
    # ("(106, 90)", "(55, 77)"),
]

os.makedirs("results", exist_ok=True)

def run_once(start, end):
    input_data = f"{start}\n{end}\n"
    try:
        result = subprocess.run(
            ["python3", "run.py"],
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10
        )
        stdout_lines = result.stdout.decode().strip().splitlines()
        stderr_lines = result.stderr.decode().strip().splitlines()

        if stderr_lines:
            print("⚠️ stderr:", "\n".join(stderr_lines))

        return stdout_lines[-1] if stdout_lines else "[EMPTY STDOUT]"

    except subprocess.TimeoutExpired:
        return "[TIMEOUT]"
    except Exception as e:
        return f"[ERROR] {str(e)}"


# Główna pętla testowa
for idx, (start, end) in enumerate(test_cases, start=10):
    filename = f"results/result_{idx}.txt"
    print(f"⏳ Test {idx}: {start} → {end} (50x) → {filename}")

    with open(filename, "w") as f:
        for i in range(50):
            last_line = run_once(start, end)
            f.write(last_line + "\n")

print("\n✅ Wszystko gotowe. Wyniki w katalogu 'results/'")
