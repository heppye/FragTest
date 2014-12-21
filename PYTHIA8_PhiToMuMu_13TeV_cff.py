import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythiaPhi = cms.vstring(
         'HardQCD:all = on',
         '333:onMode = off',
         '333:onIfMatch 13 13'),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythiaPhi')
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
~                                                                 
