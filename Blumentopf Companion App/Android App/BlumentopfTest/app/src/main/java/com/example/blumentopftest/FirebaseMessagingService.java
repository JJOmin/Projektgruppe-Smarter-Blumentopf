package com.example.blumentopftest;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        // Hier verarbeiten Sie eingehende Nachrichten
        // remoteMessage.getData() enthält die Daten der Nachricht
    }
}
