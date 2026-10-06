# Email Verification

A simple Python project that checks whether an email address is valid. It has two versions that do the same job in different ways:

- `email_validator_loops.py` uses `if` conditions and a loop to check each rule step by step.
- `email_validator_regex.py` uses a single regular expression (regex) pattern.

You only need to run one of them.

## Requirements

- Python 3 installed on your computer
- VS Code (optional, any editor works)

## How to run in VS Code

1. Download this project (click **Code**, then **Download ZIP**) and extract it.
2. Open VS Code, then go to **File > Open Folder** and select the project folder.
3. Click on `email_validator_loops.py` or `email_validator_regex.py`.
4. Click the **Run** button (triangle at the top right).
5. In the terminal at the bottom, type an email and press Enter.

## How to run in a terminal

```
python email_validator_loops.py
```
or
```
python email_validator_regex.py
```

## Example

```
Enter your Email : example@gmail.com
Right Email
```

## Known limitations

- Domains with endings longer than 3 letters or with two parts (like `.info` or `.co.in`) are rejected.
- The loops version does not allow uppercase letters.

## License

This project is licensed under the MIT License.
