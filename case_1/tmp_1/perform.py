def some_op(a, b, c):
    import torch
    from utils import add
    a = torch.tensor(a).cuda()
    b = torch.tensor(b).cuda()
    c = torch.tensor(c).cuda()
    return {"value": int(torch.pow(add(a, b), c).item())}
