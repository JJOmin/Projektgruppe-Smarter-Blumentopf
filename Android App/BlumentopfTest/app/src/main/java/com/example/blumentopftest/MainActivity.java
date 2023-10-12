package com.example.blumentopftest;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button openBrowserButton = findViewById(R.id.openBrowserButton);
        openBrowserButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Define the URL you want to open
                String url = "https://www.cloudleo.duckdns.org";

                // Create an Intent with Intent.ACTION_VIEW and the URL as data
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));

                // Start the activity with the given intent
                startActivity(intent);
            }
        });
    }
}
