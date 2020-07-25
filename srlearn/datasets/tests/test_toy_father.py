# Copyright © 2017-2020 Alexander L. Hayes

"""
Tests for the ``srlearn.datasets.ToyFather``
"""

from srlearn.datasets import ToyFather


def test_train_test_exists():
    """Check that ``ToyCancer.train`` and ``ToyCancer.test`` exist."""
    assert ToyFather.train is not None
    assert ToyFather.test is not None


def test_train_database_train_objects_exist():
    """Check for ``ToyCancer.train.pos``, ..., ``ToyCancer.train.facts``"""
    assert ToyFather.train.pos is not None
    assert ToyFather.train.neg is not None
    assert ToyFather.train.facts is not None


def test_train_database_test_objects_exist():
    """Check for ``ToyCancer.test.pos``, ..., ``ToyCancer.test.facts``"""
    assert ToyFather.test.pos is not None
    assert ToyFather.test.neg is not None
    assert ToyFather.test.facts is not None


def test_len_train_pos_and_neg():
    """Simple test for length of training data pos/neg/facts."""
    assert len(ToyFather.train.pos) == 5
    assert len(ToyFather.train.neg) == 21
    assert len(ToyFather.train.facts) == 41


def test_len_test_pos_and_neg():
    """Simple test for length of training data pos/neg/facts."""
    assert len(ToyFather.test.pos) == 3
    assert len(ToyFather.test.neg) == 4
    assert len(ToyFather.test.facts) == 11
