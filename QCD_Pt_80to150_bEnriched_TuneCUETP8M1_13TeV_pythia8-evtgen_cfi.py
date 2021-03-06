import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter(
    "Pythia8GeneratorFilter", 
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0e-4),
    crossSection = cms.untracked.double(540000000.),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            operates_on_particles = cms.vint32( 0 ), # 0 (zero) means default list (hardcoded)
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'HardQCD:all = on', 
            'PhaseSpace:pTHatMin = 80.',
            'PhaseSpace:pTHatMax = 150.',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: Configuration/Generator/python/PYTHIA8_InclMu_hardQCD8_CUEP8M1_13TeV_cff.py $'),
    annotation = cms.untracked.string('Pythia8+EvtGen130 generation, pThat = 8GeV, pT(mu) > 10GeV, 13TeV, Tune CUEP8M1')
)

# -- Filters
bFilter = cms.EDFilter(
    "PythiaFilter",
    MinPt = cms.untracked.double(0.),
    MaxPt = cms.untracked.double(9999.),
    MaxEta = cms.untracked.double(100.),
    MinEta = cms.untracked.double(-100.),
    ParticleID = cms.untracked.int32(5)
)

ProductionFilterSequence = cms.Sequence(generator*bFilter)
