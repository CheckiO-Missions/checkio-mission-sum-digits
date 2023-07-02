"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [38],
            "answer": 2
        },
        {
            "input": [0],
            "answer": 0
        },
        {
            "input": [10],
            "answer": 1
        },
        {
            "input": [132],
            "answer": 6
        },
        {
            "input": [232],
            "answer":7
        },
        {
            "input": [811],
            "answer": 1
        },
        {
            "input": [702],
            "answer": 9
        },
    ],
    "Extra": [
      {
         "input": [9615],
          "answer": 3
      },
      {
         "input": [997997997997],
          "answer": 1
      },
      {
         "input": [199],
          "answer": 1
      },
      {
         "input": [101001],
          "answer": 3
      },
      {
          "input": [999999999],
          "answer": 9
      },
    ]
}
