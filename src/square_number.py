import os

def append_to_output(var_name: str, var_value: str) -> None:
    with open(os.environ.get("GITHUB_OUTPUT"), 'a') as f:
        f.write(f'{var_name}={var_value}\n')

def main() -> None:
    num = int(os.environ.get('INPUT_NUM'))
    result = num * num
    append_to_output('num-square', str(result))

if __name__ == '__main__':
    main()
