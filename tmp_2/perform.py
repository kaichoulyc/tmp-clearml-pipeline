def some_op_1(a, b, previous_output):
    import torch
    from utils import add
    a = torch.tensor(a).cuda()
    b = torch.tensor(b).cuda()
    previous_output = torch.tensor(previous_output["value"]).cuda()
    
    return torch.pow(add(a, b), previous_output).item()
