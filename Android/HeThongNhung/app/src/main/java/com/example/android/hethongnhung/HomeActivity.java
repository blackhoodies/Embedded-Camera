package com.example.android.hethongnhung;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.messaging.FirebaseMessaging;

import pub.devrel.easypermissions.EasyPermissions;

public class HomeActivity extends AppCompatActivity {
    private TextView twStatusInfo;
    private Button btnView, btnHistory, btnSetting;
    private DatabaseReference mDatabase;

    String[] perms = {
            Manifest.permission.CAMERA,
            Manifest.permission.ACCESS_WIFI_STATE,
            Manifest.permission.CHANGE_WIFI_STATE,
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        FirebaseMessaging.getInstance().subscribeToTopic("broadcast");
        setContentView(R.layout.activity_home_new);

        if (!EasyPermissions.hasPermissions(this, perms)) {
            EasyPermissions.requestPermissions(this, getString(R.string.permission_rationale), 1, perms);
        }

        mDatabase = FirebaseDatabase.getInstance().getReference();
        mDatabase.child("status").addChildEventListener(new FirebaseChildEventListener());

        // Khoi tao TextView va dat gia tri mac dinh la NORMAL
        twStatusInfo = (TextView) findViewById(R.id.textView_status_info);
        twStatusInfo.setText("Normal");

        // Khoi tao cac bien Button
        btnView = (Button) findViewById(R.id.button_home_view);
        btnHistory = (Button) findViewById(R.id.button_home_history);
        btnSetting = (Button) findViewById(R.id.button_home_setting);

        btnView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(HomeActivity.this, ViewActivity.class));

            }
        });
        btnSetting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(HomeActivity.this, SettingActivity.class));
            }
        });
    }

    private class FirebaseChildEventListener implements ChildEventListener {
        @Override
        public void onChildAdded(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {
            String status = dataSnapshot.getValue(String.class);
            if (!status.isEmpty()){
                twStatusInfo.setText(status);
            }

        }

        @Override
        public void onChildChanged(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {
            String status = dataSnapshot.getValue(String.class);
            if (!status.isEmpty()){
                twStatusInfo.setText(status);
            }
        }

        @Override
        public void onChildRemoved(@NonNull DataSnapshot dataSnapshot) {

        }

        @Override
        public void onChildMoved(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {

        }

        @Override
        public void onCancelled(@NonNull DatabaseError databaseError) {

        }
    }
}
