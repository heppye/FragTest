# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: bJpsiX_8TeV_cfi -s GEN,SIM --conditions START50_V13::All --datatier GEN-SIM --eventcontent RAWSIM --beamspot Realistic8TeVCollision -n 100 --no_exec
import FWCore.ParameterSet.Config as cms


process.jpsifilter = cms.EDFilter("PythiaFilter",
    MaxEta = cms.untracked.double(19.9),
    Status = cms.untracked.int32(2),
    MinEta = cms.untracked.double(-19.9),
    MinPt = cms.untracked.double(6.3),
    ParticleID = cms.untracked.int32(443)
)


process.lambbafilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5122)
)


process.generator = cms.EDFilter("Pythia6GeneratorFilter",
   ExternalDecays = cms.PSet(
       EvtGen = cms.untracked.PSet(
          use_default_decay = cms.untracked.bool(False),
          decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
          particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evtLbB0Pdg11.pdl'),
          user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/LambdaB_JPsiLambda_ppi_noPol.dec'),
          list_forced_decays = cms.vstring('MyLambda_b0','Myanti-Lambda_b0'),
          operates_on_particles = cms.vint32(0)
       ),
       parameterSets = cms.vstring('EvtGen')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.00013),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(54710000000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('MSEL        = 1        ! user defined subprocess'),
        parameterSets = cms.vstring('pythiaUESettings','processParameters')
    )
)


process.mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(3.9, 3.9),
    MaxEta = cms.untracked.vdouble(2.6, 2.6),
    MinEta = cms.untracked.vdouble(-2.6, -2.6),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)


ProductionFilterSequence = cms.Sequence(generator*lambdafilter*jpsifilter*mumugenfilter)
