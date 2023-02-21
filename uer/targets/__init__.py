from uer.targets.chem_mlm_target import ChemMlmTarget
from uer.targets.mlm_target import MlmTarget
from uer.targets.lm_target import LmTarget
from uer.targets.bert_target import BertTarget
from uer.targets.cls_target import ClsTarget
from uer.targets.bilm_target import BilmTarget
from uer.targets.albert_target import AlbertTarget
from uer.targets.seq2seq_target import Seq2seqTarget
from uer.targets.t5_target import T5Target
from uer.targets.gsg_target import GsgTarget
from uer.targets.bart_target import BartTarget
from uer.targets.prefixlm_target import PrefixlmTarget


str2target = {"bert": BertTarget, "mlm": MlmTarget, "lm": LmTarget,
              "bilm": BilmTarget, "albert": AlbertTarget, "seq2seq": Seq2seqTarget,
              "t5": T5Target, "gsg": GsgTarget, "bart": BartTarget,
              "cls": ClsTarget, "prefixlm": PrefixlmTarget, "chemmlm": ChemMlmTarget}

__all__ = ["BertTarget", "MlmTarget", "LmTarget", "BilmTarget", "AlbertTarget",
           "Seq2seqTarget", "T5Target", "GsgTarget", "BartTarget", "ClsTarget", "PrefixlmTarget", "ChemMlmTarget", "str2target"]
