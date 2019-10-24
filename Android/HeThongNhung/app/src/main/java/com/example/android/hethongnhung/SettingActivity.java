package com.example.android.hethongnhung;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.android.hethongnhung.Controller.StoreData;
import com.example.android.hethongnhung.Controller.Utils;

public class SettingActivity extends AppCompatActivity {
    private EditText ipAddress, port;
    private Button btn_save;
    private Context context;

    private final String TAG = SettingActivity.class.getName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_setting);

        context = this;

        ipAddress = (EditText) findViewById(R.id.editText_setting_ipAddress);
        port = (EditText) findViewById(R.id.editText_setting_port);

        btn_save = (Button) findViewById(R.id.button_setting_save);
        btn_save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String ipAddressVal = ipAddress.getText().toString();
                String portVal = port.getText().toString();

                if (!Utils.checkIPAddress(ipAddressVal)) {
                    Toast.makeText(context, "Nhập vào địa chỉ IP hợp lệ...", Toast.LENGTH_SHORT).show();
                    return;
                }
                if (!Utils.checkPortNumber(portVal)) {
                    Toast.makeText(context, "Nhập vào số cổng hợp lệ...", Toast.LENGTH_SHORT).show();
                    return;
                }

                StoreData.saveData(context, ipAddressVal, Integer.parseInt(portVal));
                finish();
            }
        });
    }
}
