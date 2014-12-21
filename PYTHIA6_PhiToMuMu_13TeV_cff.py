import FWCore.ParameterSet.Config as cms
from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(0.49),
    crossSection = cms.untracked.double(54000000000),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=2          ! Default',
        'BRAT(656)=0 ! decay forbidden',
        'BRAT(657)=0 ! decay dimuon',
        'BRAT(658)=0 ! decay forbidden',
        'BRAT(659)=0 ! decay forbidden',
        'BRAT(660)=0 ! decay forbidden',
        'BRAT(661)=0 ! decay forbidden',
        'BRAT(662)=0 ! decay forbidden',
        'BRAT(663)=0 ! decay forbidden',
        'BRAT(664)=0 ! decay forbidden',
        'BRAT(665)=1 ! mumu',
        'BRAT(666)=0 ! decay forbidden',
        'MDME(656,1)=0 ! ',
        'MDME(657,1)=0 ! ',
        'MDME(658,1)=0 ! ',
        'MDME(659,1)=0 ! ',
        'MDME(660,1)=0 ! ',
        'MDME(661,1)=0 ! ',
        'MDME(662,1)=0 ! ',
        'MDME(663,1)=0 ! ',
        'MDME(664,1)=0 ! ',
        'MDME(665,1)=1 ! ',
        'MDME(666,1)=0 ! '),
        parameterSets = cms.vstring('pythiaUESettings',
                        'processParameters')
        )
        )
phifilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(1000.0),
    MinEta = cms.untracked.double(-1000.0),
    MinPt = cms.untracked.double(0.0),
    ParticleID = cms.untracked.int32(333)
)



ProductionFilterSequence = cms.Sequence(generator*phifilter)
