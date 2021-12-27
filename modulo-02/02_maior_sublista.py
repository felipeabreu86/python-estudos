def sub_seq_max2(seq):
    max_geral = max_atual = 0
    for n in seq:
        max_atual = max((max_atual + n, n))
        max_geral = max((max_geral, max_atual))
    return max_geral


print(sub_seq_max2([-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]))  # Resultado 13
