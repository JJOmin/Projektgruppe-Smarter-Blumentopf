<?php 

// Web-API for writing & saving data to JSON file on server

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE');

$prototype = json_decode(file_get_contents('prototyp.json'), true);
$data = json_decode(file_get_contents('php://input'), true);

if (isset($data)) {

    array_push($prototype['timeStamps'], $data['timeStamp']);
    array_push($prototype['sensors']['temperature']['log'], $data['temperature']);
    array_push($prototype['sensors']['light']['log'], $data['light']);
    array_push($prototype['sensors']['moisture']['log'], $data['moisture']);

    $jsonData = json_encode($prototype, JSON_PRETTY_PRINT);
    file_put_contents('prototyp.json', $jsonData);

    echo json_encode(['status' => 'success', 'message' => $prototype]);
} else {
    echo json_encode(['status' => 'error', 'message' => 'Could not update Json!']);
}

?>