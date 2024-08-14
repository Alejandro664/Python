def progress_bar (part, total, tamano = 30):
    frac = part / total
    completed = int (frac * tamano)
    missing = tamano - completed
    bar = f"[{'🦁'*completed}{'-'*missing}]{frac:.2%}"
    return bar