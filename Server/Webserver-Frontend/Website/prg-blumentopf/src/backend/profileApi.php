<?php 

// Web-API for reading profile data from JSON file on server

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE');

$prototype = json_decode(file_get_contents('prototyp.json'), true);
$profiles = json_decode(file_get_contents('db.json'), true);
$selectedPlant = $prototype['selectedPlant'];

$activeProfile = [];

foreach ($profiles['profiles'] as $key => $value) {
    if ($key === $selectedPlant) {
        $activeProfile = [$key => $value];
    }
}

foreach ($prototype['profiles'] as $key => $value) {
    if ($key === $selectedPlant) {
        $activeProfile = [$key => $value];
    }
}

if ($activeProfile != []) {
    $jsonData = json_encode($activeProfile, JSON_PRETTY_PRINT);
    echo $jsonData;
} else {
    echo json_encode(['status' => 'error', 'message' => 'Could not get profile!']);
}

/*
$data = json_decode(file_get_contents('php://input'), true);

if (isset($data)) {
    $jsonData = json_encode($data, JSON_PRETTY_PRINT);
    file_put_contents('prototyp.json', $jsonData);
    echo json_encode(['status' => 'success', 'message' => 'Successfully updated Json!']);
} else {
    echo json_encode(['status' => 'error', 'message' => 'Could not update Json!']);
}
*/

?>