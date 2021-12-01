import json

THRESHOLD = .93

def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = event['inferences'] ## TODO: fill in

    # Check if any values in our inferences are above THRESHOLD
    if inferences[0] > 0.7:
        meets_threshold = True
    else:
        meets_threshold = False ## TODO: fill in

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise TypeError("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }