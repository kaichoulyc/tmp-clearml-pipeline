def some_op_1(a, b, previous_output):
    import torch
    from utils import add

    from tmp_3.utils import exp_it

    a = torch.tensor(a).cuda()
    b = torch.tensor(b).cuda()
    previous_output = torch.tensor(previous_output["value"]).cuda()

    1 / 0

    kl = torch.pow(add(a, b), previous_output).item()

    return {"value": exp_it(kl, 2)}
