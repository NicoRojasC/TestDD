from dataclasses import dataclass


@dataclass
class InputCore():
    totalized_exclusions : dict
    level_compliance_defined : dict
    rules_scaned : dict
    scope_pipeline : str