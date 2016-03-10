import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *


generator = cms.EDProducer("FlatRandomPtGunProducer",
    pythiaPylistVerbosity = cms.untracked.int32(10),
    maxEventsToPrint = cms.untracked.int32(10),
    PGunParameters = cms.PSet(
        MaxPt = cms.double(2000.0),
        MinPt = cms.double(0.0),
        PartID = cms.vint32(5),
        MaxEta = cms.double(10.0),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-10.0),
        MinPhi = cms.double(-3.14159265359) ## in radians
    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts
    psethack = cms.string('single b pt 0-2000'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1),
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
        processParameters=EvtGenExtraParticles,
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

#generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)



ProductionFilterSequence = cms.Sequence(generator)
