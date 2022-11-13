from random import sample
def get_random_password() -> str:
    alpha_low = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    str_passw = sample(alpha_low, 8)

    return "".join([str(numb) for numb in str_passw])

print(get_random_password())


