# CountSnpEffAnnotationsPerGene
A script to identify genes with a snpEff impact annotation from an annotated VCF file (with counts).

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- requirements -->
## Requirements

This script has been tested with Python 3.
The script requires a vcf file (version 4.2 tested) that has been annotated with snpEff (version 5.0e tested).

<!-- usage -->
## Usage

1) Generate a list of genes with counts of the selected impact annotation (MODIFIER, LOW, MEDIUM, or HIGH):<br /><br />
&nbsp;&nbsp;&nbsp;python GenesWithSnpEffImpact.v1.0.py -file file.vcf.gz -out HIGH > HighOutput.txt<br /><br />
&nbsp;&nbsp;&nbsp;help (and further explanations): python GenesWithSnpEffImpact.v1.0.py -h


<!-- license -->
## License 

Distributed under the MIT License.
