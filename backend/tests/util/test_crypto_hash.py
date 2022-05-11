from backend.util.crypto_hash import  crypto_hash


def test_crypto_hash():
    #it should create the same hash with arguments of differentn data types
    #in any order
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', 1, [2])
    assert crypto_hash('123') =='3140d59420ca920c79fdef003360543c12b14da984f00f8665756e9da9c4b743'