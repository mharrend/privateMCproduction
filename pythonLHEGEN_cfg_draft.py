# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/HIG-RunIISummer15wmLHEGS-00597-fragment.py --fileout file:HIG-RunIISummer15wmLHEGS-00597.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN:ProductionFilterSequence,SIM --magField 38T_PostLS1 --python_filename HIG-RunIISummer15wmLHEGS-00597_1_cfg.py --no_exec -n 41
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(#NUMBEREVENTS#)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/pythonLHEGEN.py nevts:100'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:eventLHEGEN-output.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.LHEEventContent.outputCommands,
    fileName = cms.untracked.string('file:eventLHEGEN-output_inLHE.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('LHE')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.selectedHadronsAndPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    src = cms.InputTag("generator"),
    partonMode = cms.string('Auto')
)


process.genJetFlavourInfos = cms.EDProducer("JetFlavourClustering",
    ghostRescaling = cms.double(1e-18),
    partons = cms.InputTag("selectedHadronsAndPartons","partons"),
    jetAlgorithm = cms.string('AntiKt'),
    bHadrons = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
    rParam = cms.double(0.4),
    jets = cms.InputTag("ak4GenJetsCustom"),
    hadronFlavourHasPriority = cms.bool(True),
    cHadrons = cms.InputTag("selectedHadronsAndPartons","cHadrons")
)


process.ttHFGenFilter = cms.EDFilter("ttHFGenFilter",
    genBHadFlavour = cms.InputTag("matchGenBHadron","genBHadFlavour"),
    genBHadFromTopWeakDecay = cms.InputTag("matchGenBHadron","genBHadFromTopWeakDecay"),
    genBHadPlusMothers = cms.InputTag("matchGenBHadron","genBHadPlusMothers"),
    genBHadIndex = cms.InputTag("matchGenBHadron","genBHadIndex"),
    OnlyHardProcessBHadrons = cms.bool(False),
    genBHadPlusMothersIndices = cms.InputTag("matchGenBHadron","genBHadPlusMothersIndices"),
    genParticles = cms.InputTag("genParticles")
)


process.matchGenBHadron = cms.EDProducer("GenHFHadronMatcher",
    jetFlavourInfos = cms.InputTag("genJetFlavourInfos"),
    flavour = cms.int32(5),
    noBBbarResonances = cms.bool(False),
    genParticles = cms.InputTag("genParticles"),
    onlyJetClusteredHadrons = cms.bool(False)
)


process.ak4GenJetsCustom = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    doAreaFastjet = cms.bool(False),
    Ghost_EtaMax = cms.double(6.0),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('GenJet'),
    minSeed = cms.uint32(14327),
    doRhoFastjet = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.4),
    maxProblematicHcalCells = cms.uint32(9999999),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8PowhegEmissionVetoSettings = cms.vstring('POWHEG:veto = 1', 
            'POWHEG:pTdef = 1', 
            'POWHEG:emitted = 0', 
            'POWHEG:pTemt = 0', 
            'POWHEG:pThard = 0', 
            'POWHEG:vetoCount = 100', 
            'SpaceShower:pTmaxMatch = 2', 
            'TimeShower:pTmaxMatch = 2'),
        processParameters = cms.vstring('POWHEG:nFinal = 2', 
            'TimeShower:mMaxGamma = 1.0', 
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'SpaceShower:alphaSvalue=0.1108', 
            'PDF:pSet=LHAPDF6:NNPDF30_lo_as_0130', 
            'MultipartonInteractions:pT0Ref=2.034340e+00', 
            'MultipartonInteractions:expPow=1.932600e+00', 
            'ColourReconnection:range=5.706919e+00'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8PowhegEmissionVetoSettings', 
            'processParameters')
    )
)


process.ak4GenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    src = cms.InputTag("genParticlesForJets"),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(6.0),
    doRhoFastjet = cms.bool(False),
    srcPVs = cms.InputTag(""),
    inputEtMin = cms.double(0.0),
    doAreaFastjet = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.5),
    jetPtMin = cms.double(3.0),
    inputEMin = cms.double(0.0),
    jetType = cms.string('GenJet'),
    doPUOffsetCorr = cms.bool(False),
    radiusPU = cms.double(0.5),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxBadEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.4)
)


process.genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    src = cms.InputTag("genParticles"),
    ignoreParticleIDs = cms.vuint32(1000022, 1000012, 1000014, 1000016, 2000012, 
        2000014, 2000016, 1000039, 5100039, 4000012, 
        4000014, 4000016, 9900012, 9900014, 9900016, 
        39, 12, 14, 16),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(False),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)


process.ak4JetFlavourInfos = cms.EDProducer("JetFlavourClustering",
    ghostRescaling = cms.double(1e-18),
    partons = cms.InputTag("selectedHadronsAndPartons","partons"),
    jetAlgorithm = cms.string('AntiKt'),
    bHadrons = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
    rParam = cms.double(0.4),
    jets = cms.InputTag("ak4PFJets"),
    hadronFlavourHasPriority = cms.bool(True),
    cHadrons = cms.InputTag("selectedHadronsAndPartons","cHadrons")
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(#NUMBEREVENTS#),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    args = cms.vstring('#GRIDPACKLOCATION#')
)


process.ProductionFilterSequence = cms.Sequence(process.generator+cms.SequencePlaceholder("pgen")+process.selectedHadronsAndPartons+process.genParticlesForJetsNoNu+process.ak4GenJetsCustom+process.genJetFlavourInfos+process.matchGenBHadron+process.ttHFGenFilter)

# Set different random numbers seeds every time one runs cmsRun
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()


# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.ProductionFilterSequence)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step,process.LHEoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
