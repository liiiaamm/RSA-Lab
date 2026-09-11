# RSA Lab

**Explore the mathematics of public-key cryptography.**

An educational Python implementation of RSA, with number-theory utilities, character encoding, a local command-line messaging exercise, and cryptanalysis demonstrations.

## What is inside

- Prime generation and RSA key construction.
- Integer and string encryption / decryption.
- An experimental decimal-padding scheme.
- Key-registration and local message-exchange scripts.
- Factorization and chosen-plaintext exercises.

## Quick start

Use Python 3.11. The core modules use the standard library; `rsa` refers to the local `rsa.py`, so no third-party RSA package is required.

From the repository root, try these **public textbook parameters**:

```python
from rsa import cifrar_rsa, descifrar_rsa

n, e, d = 3233, 17, 2753
ciphertext = cifrar_rsa(65, n, e, 0)
plaintext = descifrar_rsa(ciphertext, n, d, 0)
print(ciphertext, plaintext)  # 2790 65
```

## Repository map

| File | Purpose |
| --- | --- |
| `rsa.py` | RSA operations and attack demonstrations |
| `modular.py` | Number-theory helpers |
| `registrarusuario.py` | Interactive generation of local user key files |
| `criptochat.py` | Local encryption / decryption interface |
| `pruebas.py` | Original experimentation script |

## Educational scope

This implementation uses Python's `random` module and a custom decimal-padding scheme, not a standardized secure construction such as OAEP. It is intended for learning, not protecting real messages or credentials. Historical example keys committed to this repository are public and must never be reused. Generate exercise keys locally and keep them out of commits.

The original interactive tools and key-generation edge cases need further validation. The small example above demonstrates the core integer round trip.

## Authors

**Liam Esgueva González and Sergio Fernández Cordero** · Discrete Mathematics · Comillas ICAI.
