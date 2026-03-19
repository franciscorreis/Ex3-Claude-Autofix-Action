import string

from functions.validar_password import validar_password

# Blocos de caracteres por classe
_UPPER   = string.ascii_uppercase   # A-Z
_LOWER   = string.ascii_lowercase   # a-z
_SPECIAL = string.punctuation       # !"#$%...
_DIGIT   = string.digits            # 0-9

def _build(upper=0, lower=0, special=0, digit=0, pad=0):
    """Constrói uma password com exatamente os caracteres pedidos."""
    return (
        _UPPER[0]   * upper   +
        _LOWER[0]   * lower   +
        _SPECIAL[0] * special +
        _DIGIT[0]   * digit   +
        _LOWER[1]   * pad
    )

def test_password_valida():
    # 10 chars: maiúscula, minúscula, especial, dígito + padding
    pw = _build(upper=1, lower=1, special=1, digit=1, pad=6)
    assert len(pw) == 10
    assert validar_password(pw) == True

def test_password_minimo_exato():
    # exatamente 8 chars cumprindo todos os requisitos
    pw = _build(upper=1, lower=1, special=1, digit=1, pad=4)
    assert len(pw) == 8
    assert validar_password(pw) == True

def test_password_sem_maiuscula():
    pw = _build(lower=1, special=1, digit=1, pad=5)
    assert len(pw) >= 8
    assert validar_password(pw) == False

def test_password_sem_minuscula():
    pw = _build(upper=5, special=1, digit=2)
    assert len(pw) >= 8
    assert validar_password(pw) == False

def test_password_sem_especial():
    pw = _build(upper=1, lower=1, digit=1, pad=5)
    assert len(pw) >= 8
    assert validar_password(pw) == False

def test_password_muito_curta():
    pw = _build(upper=1, lower=1, special=1)
    assert len(pw) == 3
    assert validar_password(pw) == False

def test_password_curta():
    pw = _build(upper=1, lower=1, special=1, digit=1, pad=2)
    assert len(pw) == 6
    assert validar_password(pw) == True