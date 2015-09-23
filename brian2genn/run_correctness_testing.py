import brian2genn
from brian2.tests.features import (Configuration, DefaultConfiguration,
                                   run_feature_tests, run_single_feature_test)
from brian2genn.correctness_testing import GeNNConfiguration

from brian2.tests.features.synapses import *
from brian2.tests.features.neurongroup import *
from brian2.tests.features.monitors import *
from brian2.tests.features.speed import *
from brian2.tests.features.input import *
from brian2.tests.features import CPPStandaloneConfiguration
from brian2 import prefs

prefs.codegen.loop_invariant_optimisations = False
prefs.devices.genn.connectivity = 'AUTO'
prefs.core.network.default_schedule= ['start', 'synapses', 'groups', 'thresholds', 'resets', 'end']
prefs.devices.genn.unix_compiler_flags="-O1"
prefs.devices.genn.cpu_only=True

if __name__=='__main__':
    #c = GeNNConfiguration()
    #c.before_run()
    #f = SynapsesPre()
    #f.run()
    #c.after_run()
    #print run_single_feature_test(CPPStandaloneConfiguration, SynapsesSTDP)
    #print run_single_feature_test(GeNNConfiguration, SpikeGeneratorGroupTest)
    #print run_single_feature_test(CPPStandaloneConfiguration, NeuronGroupLIFRefractory)
    #print run_single_feature_test(DefaultConfiguration, SynapsesPost)
    #print run_feature_tests(configurations=[DefaultConfiguration,
    #                                        GeNNConfiguration],
    #                        feature_tests=[SynapsesPre,
    #                                       SynapsesPost]).tables_and_exceptions
    #print run_feature_tests(configurations=[DefaultConfiguration, 
    #                                         GeNNConfiguration],
    #                         feature_tests=[NeuronGroupIntegrationLinear]).tables_and_exceptions
    print run_feature_tests(configurations=[DefaultConfiguration,GeNNConfiguration,CPPStandaloneConfiguration],feature_tests=[ 
        #run_feature_tests(configurations=[GeNNConfiguration], feature_tests=[ 
        NeuronGroupIntegrationLinear, NeuronGroupIntegrationEuler, NeuronGroupLIF, NeuronGroupLIFRefractory, SynapsesPre, SynapsesPost,
        # SynapsesSTDPNoAutapse, 
        SynapsesSTDP, 
        SpikeMonitorTest,
        StateMonitorTest, SpikeGeneratorGroupTest 
    ]).tables_and_exceptions
    #print run_feature_tests(configurations=[DefaultConfiguration,
    #                                        GeNNConfiguration], feature_tests=[SynapsesSTDP]).tables_and_exceptions
    #print run_single_feature_test(CPPStandaloneConfiguration, SpikeMonitorTest)
    #print run_single_feature_test(GeNNConfiguration, SpikeMonitorTest)
