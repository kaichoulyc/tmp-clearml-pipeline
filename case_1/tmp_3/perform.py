def some_op_2(a, b, previous_output, previous_output_2):
    import torch
    from utils import add

    from tmp_3.utils import exp_it
    a = torch.tensor(a).cuda()
    b = torch.tensor(b).cuda()
    previous_output = torch.tensor(previous_output["value"]).cuda()

    print(3)
    
    return exp_it(torch.pow(add(a, b), previous_output).item(), previous_output_2["value"])
