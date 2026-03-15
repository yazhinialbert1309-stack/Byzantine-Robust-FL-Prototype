"""
Config for Robust FL for Privacy-Preserving CTI.
Industrial networks - Krum / Trimmed Mean aggregation.
"""
from dataclasses import dataclass
from typing import Literal

@dataclass
class Config:
    # FL
    num_clients: int = 5
    num_rounds: int = 20
    fraction_fit: float = 1.0  # use all clients each round
    min_fit_clients: int = 2
    
    # Robust aggregation: "fedavg" | "krum" | "trimmed_mean"
    aggregation: Literal["fedavg", "krum", "trimmed_mean"] = "fedavg"
    # Krum: number of Byzantine workers to tolerate (f)
    krum_f: int = 1
    # Trimmed Mean: fraction to trim each side (e.g. 0.1 = trim 10% smallest, 10% largest)
    trimmed_mean_beta: float = 0.1
    
    # Malicious clients (for evaluation)
    num_malicious: int = 1
    poison_scale: float = -5.0  # malicious scale gradient (flip / degrade)
    
    # Data
    data_path: str = ""  # if empty, use synthetic CTI-like data
    n_features: int = 78   # CIC-IDS2017-like feature count
    num_classes: int = 2   # binary: normal vs attack
    non_iid_alpha: float = 0.5  # Dirichlet alpha for non-IID (smaller = more heterogeneous)
    train_ratio: float = 0.7
    val_ratio: float = 0.15
    
    # Model & training
    hidden_sizes: tuple = (64, 32)
    lr: float = 0.01
    batch_size: int = 32
    local_epochs: int = 2
    
    # Differential Privacy (optional)
    use_dp: bool = False
    dp_epsilon: float = 1.0
    dp_delta: float = 1e-5
    max_grad_norm: float = 1.0

config = Config()
