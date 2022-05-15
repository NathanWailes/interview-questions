
if __name__ == '__main__':
    answer = topNCompetitors(999, 2, ['a'], 999, ['a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['a', 'a'], 999, ['a', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['b', 'a'], 999, ['a', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['b', 'a'], 999, ['ab', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['ba', 'a'], 999, ['b', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2,
        [
            'anacell',
            'betacellular',
            'certracular',
            'deltacellular',
            'eurocell'
        ],
        3,
        [
            'Best services provided by anacell',
            'betacellular has great services',
            'anacell provides much better services than all other'
        ]
    )
    print(answer)
    assert(answer == ['anacell', 'betacellular'])

    answer = topNCompetitors(
        999,
        2,
        [
            'anacell',
            'betacellular',
            'certracular',
            'deltacellular',
            'eurocell'
        ],
        3,
        [
            'eurocell',
            'eurocell',
            'betacellular has great services',
            'Best services provided by anacell',
            'anacell provides much better services than all other',
            'betacellular has great services',
        ]
    )
    print(answer)
    assert(answer == ['anacell', 'betacellular'])

    answer = topNCompetitors(
        999,
        2,
        [
            'anacell',
            'betacellular',
            'certracular',
        ],
        3,
        [
            'anacell',
            'betacellular',
            'betacellular',
            'certracular',
            'certracular',
            'certracular',
        ]
    )
    print(answer)
    assert(answer == ['certracular', 'betacellular'])
