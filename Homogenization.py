from abaqus import *
from abaqusConstants import *
import os
import job
from odbAccess import *	
import string
import visualization
from textRepr import *
import numpy as np
import regionToolset

odbname='Job-1.odb'
odb = openOdb(odbname)
scratchOdb = session.ScratchOdb(odb)
datum=scratchOdb.rootAssembly.DatumCsysByThreePoints(name='CSYS-1', coordSysType=CARTESIAN,origin=(0.0, 0.0, 0.0), point1=(0.0, 0.0, 1.0), point2=(0.0, 1.0, 0.0))

for i in range(len(odb.rootAssembly.instances)):
    Stepname='Step-'+str(i+1)
    if i==0:
        InstanceName='PART-PLATE-1'
    Instance=odb.rootAssembly.instances[InstanceName]
    for frame in range(len(odb.steps[Stepname].frames)):
        StressFieldOutput=odb.steps[Stepname].frames[frame].fieldOutputs['S'] # Stress FieldOutput
        StressField=StressFieldOutput.getTransformedField(datumCsys=datum)
        Field1 = StressField.getSubset(region=Instance, position=INTEGRATION_POINT)
        field1Values = Field1.values

        StrainFieldOutput=odb.steps[Stepname].frames[frame].fieldOutputs['EE'] # Strain FieldOutput
        StrainField=StrainFieldOutput.getTransformedField(datumCsys=datum)
        Field2 = StrainField.getSubset(region=Instance, position=INTEGRATION_POINT)
        field2Values = Field2.values

        IvolFieldOutput=odb.steps[Stepname].frames[frame].fieldOutputs['IVOL'] # Strain FieldOutput
        IvolField=IvolFieldOutput.getTransformedField(datumCsys=datum)
        Field3 = IvolField.getSubset(region=Instance, position=INTEGRATION_POINT)
        field3Values = Field3.values

        EvolFieldOutput=odb.steps[Stepname].frames[frame].fieldOutputs['EVOL'] # Strain FieldOutput
        EvolField=EvolFieldOutput.getTransformedField(datumCsys=datum)
        Field4 = EvolField.getSubset(region=Instance, position=INTEGRATION_POINT)
        field4Values = Field4.values


