def reemplazar_simbolo(w,a,b):
    if w == "":
        return w
    if w[-1] == a:
        return reemplazar_simbolo(w[:-1],a,b) + b
    else:
        return reemplazar_simbolo(w[:-1],a,b) + w[-1]
