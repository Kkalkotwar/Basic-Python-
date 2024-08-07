import logging
logging.basicConfig(filename='Test1.log', level=logging.INFO)
logging.info('This is my first Log File')

# There is the Hirerchy in the logging,
# Following Logging Hirerchy Must be followed

"""
Different type of level of log:

    1. logging.INFO             # 10
    2. logging.debug            # 20
    3. logging.warning          # 30
    4. logging.error            # 40
    5. logging.critical         # 50
"""

