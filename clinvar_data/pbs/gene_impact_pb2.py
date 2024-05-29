# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clinvar_data/pbs/gene_impact.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clinvar_data.pbs import (
    clinvar_public_pb2 as clinvar__data_dot_pbs_dot_clinvar__public__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n"clinvar_data/pbs/gene_impact.proto\x12\x1c\x63linvar_data.pbs.gene_impact\x1a%clinvar_data/pbs/clinvar_public.proto"\xdb\x02\n\x10GeneImpactCounts\x12\x0f\n\x07hgnc_id\x18\x01 \x01(\t\x12R\n\rimpact_counts\x18\x02 \x03(\x0b\x32;.clinvar_data.pbs.gene_impact.GeneImpactCounts.ImpactCounts\x1a\xe1\x01\n\x0cImpactCounts\x12=\n\x0bgene_impact\x18\x01 \x01(\x0e\x32(.clinvar_data.pbs.gene_impact.GeneImpact\x12\x14\n\x0c\x63ount_benign\x18\x02 \x01(\r\x12\x1b\n\x13\x63ount_likely_benign\x18\x03 \x01(\r\x12$\n\x1c\x63ount_uncertain_significance\x18\x04 \x01(\r\x12\x1f\n\x17\x63ount_likely_pathogenic\x18\x05 \x01(\r\x12\x18\n\x10\x63ount_pathogenic\x18\x06 \x01(\r*\xf9\x04\n\nGeneImpact\x12\x1b\n\x17GENE_IMPACT_UNSPECIFIED\x10\x00\x12\'\n#GENE_IMPACT_THREE_PRIME_UTR_VARIANT\x10\x01\x12&\n"GENE_IMPACT_FIVE_PRIME_UTR_VARIANT\x10\x02\x12-\n)GENE_IMPACT_DOWNSTREAM_TRANSCRIPT_VARIANT\x10\x03\x12"\n\x1eGENE_IMPACT_FRAMESHIFT_VARIANT\x10\x04\x12\x1d\n\x19GENE_IMPACT_INFRAME_INDEL\x10\x05\x12\x1a\n\x16GENE_IMPACT_START_LOST\x10\x06\x12\x1e\n\x1aGENE_IMPACT_INTRON_VARIANT\x10\x07\x12 \n\x1cGENE_IMPACT_MISSENSE_VARIANT\x10\x08\x12-\n)GENE_IMPACT_NON_CODING_TRANSCRIPT_VARIANT\x10\t\x12\x1b\n\x17GENE_IMPACT_STOP_GAINED\x10\n\x12&\n"GENE_IMPACT_NO_SEQUENCE_ALTERATION\x10\x0b\x12\'\n#GENE_IMPACT_SPLICE_ACCEPTOR_VARIANT\x10\x0c\x12$\n GENE_IMPACT_SPLICE_DONOR_VARIANT\x10\r\x12\x19\n\x15GENE_IMPACT_STOP_LOST\x10\x0e\x12"\n\x1eGENE_IMPACT_SYNONYMOUS_VARIANT\x10\x0f\x12+\n\'GENE_IMPACT_UPSTREAM_TRANSCRIPT_VARIANT\x10\x10*\xd6\x02\n\x14\x43linicalSignificance\x12%\n!CLINICAL_SIGNIFICANCE_UNSPECIFIED\x10\x00\x12 \n\x1c\x43LINICAL_SIGNIFICANCE_BENIGN\x10\x01\x12\'\n#CLINICAL_SIGNIFICANCE_LIKELY_BENIGN\x10\x02\x12\x30\n,CLINICAL_SIGNIFICANCE_UNCERTAIN_SIGNIFICANCE\x10\x03\x12+\n\'CLINICAL_SIGNIFICANCE_LIKELY_PATHOGENIC\x10\x04\x12$\n CLINICAL_SIGNIFICANCE_PATHOGENIC\x10\x05\x12&\n"CLINICAL_SIGNIFICANCE_NOT_PROVIDED\x10\x06\x12\x1f\n\x1b\x43LINICAL_SIGNIFICANCE_OTHER\x10\x07\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "clinvar_data.pbs.gene_impact_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_GENEIMPACT"]._serialized_start = 458
    _globals["_GENEIMPACT"]._serialized_end = 1091
    _globals["_CLINICALSIGNIFICANCE"]._serialized_start = 1094
    _globals["_CLINICALSIGNIFICANCE"]._serialized_end = 1436
    _globals["_GENEIMPACTCOUNTS"]._serialized_start = 108
    _globals["_GENEIMPACTCOUNTS"]._serialized_end = 455
    _globals["_GENEIMPACTCOUNTS_IMPACTCOUNTS"]._serialized_start = 230
    _globals["_GENEIMPACTCOUNTS_IMPACTCOUNTS"]._serialized_end = 455
# @@protoc_insertion_point(module_scope)
