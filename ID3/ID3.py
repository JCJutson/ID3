
def make_tree(data, classes, featureNames):
    #Various initialisations
    default = classes[argmax(frequency)]
    if nData == 0 or nFeatures == 0:
        #Have reached an empty branch
        return default
    elif classes.count(classes[0]) == nData:
        #only 1 class remains
        return classes[0]
    else:
        #choose which feature is best
        gain = zeros(nFeatures)
        for feature in range(nFeatures):
            g = calc_info_gain(data, classes, feature)
            gain[feature] = totalEntropy - g

        bestFeature = argmax(gain)
        tree = {featureNames[bestFeature]:{}}
        #Find the possible feature values
        for value in values:
            #Find datapoints with each feature value
            for datapoint in data:
                if datapoint[bestFeature] == value:
                    if bestFeature == 0:
                        datapoint = datapoint[1:]
                        newNames = featureNames[1:]
                    elif bestFeature == nFeatures:
                        datapoint = datapoint[:-1]
                        newNames = featureNames[:-1]
                    else:
                        datapoint = datapoint[:bestFeature]
                        datapoint.extend(datapoint[bestFeature+1:])
                        newNames = featureNames[:bestFeature]
                        newNames.extend(featureNames[bestFeature+1:])
                    newData.append(datapoint)
                    newClasses.append(classes[index])
                index += 1
            #Now recurse to the next level
            subtree = make_tree(NewData, newClasses, newNames)
            #And on returning, add the subtree on to the tree
            tree[featureNames[bestFeature]][value] = subtree
        return tree

def calc_info_gain(data, classes, feature):
    gain = 0
    nData = len(data)
    #List the values that feature can take
    values = []
    for datapoint in data:
        if values.count(datapoint[feature]) == 0:
            values.append(datapoind[feature])
   
    featureCounts = zeros(len(values))
    entropy = zeros(len(values))
    valueIndex = 0
    #Find where those values appear in data[feature] and the corresponding class
    for value in values:
        dataIndex = 0
        newClasses = []
        for datapoint in data:
            if datapoint[feature] == value:
                featureCounts[valueIndex] += 1
                newClasses.append(classes[dataIndex])
            dataIndex += 1
        # Get the values in newClasses
        classValues = []
        for aclass in newClasses:
            if classValues.count(aclass) == 0:
                classValues.append(aclass)

        classCounts = zeros(len(classValues))
        classIndex = 0
        for classValue in classValues:
            for aclass in newClasses:
                if aclass == classValue:
                    classCount[classIndex] += 1
            classIndex += 1

        for classIndex in range(len(classValues)):
            entropy[valueIndex] += calc_entropy(float(classCounts[classIndex])/sum(classCounts))
        gain += float(featureCounts[valueIndex])/nData * entropy[valueIndex]
        valueIndex =+ 1
    return gain

def calc_entropy(p):
    
    if p != 0:
        return -p * log2(p)
    else:
        return 0

numFeatures = input()
features = []
answers = []
for nF in range(0, numFeatures):
    newf = raw_input()
    features.append(newf)
answers.append(raw_input())

for f in range(0, numFeatures):
    print(features[f])




