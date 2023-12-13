<?php 
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE');

$data = json_decode(file_get_contents('php://input'), true);

if (isset($data)) {
    $jsonData = json_encode($data, JSON_PRETTY_PRINT);
    file_put_contents('prototyp.json', $jsonData);
    echo json_encode(['status' => 'success', 'message' => 'Successfully updated Json!']);
} else {
    echo json_encode(['status' => 'error', 'message' => 'Could not update Json!']);
}

?>