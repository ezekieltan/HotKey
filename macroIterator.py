def runMacros(hks, down, recentOperations):
    try:
        hit = False
        for hk in hks:
            for macroName, macro in hk.getMacros().items():
                if ('keys' in macro):
                    expectedKeys = macro['keys']
                    expectedDict = {key: True for key in expectedKeys}
                    selectiveDown = {key: value for key, value in down.items() if value is True}
                    if (hk.ignoreFn and 'FN' in selectiveDown):
                        del selectiveDown['FN']
                    if (selectiveDown == expectedDict):
                        hit = True
                elif ('sequences' in macro):
                    sequences = macro['sequences']
                    lastN = recentOperations.getLastNItems(len(sequences[0]))
                    if lastN in sequences:
                        hit = True
                else:
                    return False  # for future types # pragma: no cover
                if (hit):
                    print("HIT")
                    try:
                        hk.execute(macroName)
                        return macro['block'] if 'block' in macro else True
                    except Exception as e:
                        exceptionHandler('execution', type(e), e)
                        return macro['block'] if 'block' in macro else True

    except Exception as e:
        exceptionHandler('run', type(e), e)
        return False
    return False


def exceptionHandler(f, t, e):
    print(f + " error (" + str(t) + "): " + str(e))  # pragma: no cover
