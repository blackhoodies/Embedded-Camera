package com.example.android.hethongnhung;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.android.hethongnhung.Controller.Utils;

public class MainActivity extends AppCompatActivity {
    EditText editText_ipAddress, editText_portNumber;
    Button button_enter;
    WebView webView;
    Context context;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Lưu trữ giá trị Context để sử dụng được trong inner class
        context = this;

        // Khởi tạo các đối tượng View
        editText_ipAddress = (EditText) findViewById(R.id.editText_ipAddress);
        editText_portNumber = (EditText) findViewById(R.id.editText_port);
        button_enter = (Button) findViewById(R.id.button_enter);
        webView = (WebView) findViewById(R.id.webView);
        webView.setVisibility(View.INVISIBLE);

        button_enter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String ipAddress = editText_ipAddress.getText().toString();
                String portNumber = editText_portNumber.getText().toString();
                if (!Utils.checkIPAddress(ipAddress)) {
                    Toast.makeText(context, "Nhập vào địa chỉ IP hợp lệ...", Toast.LENGTH_SHORT).show();
                    return;
                }
                if (!Utils.checkPortNumber(portNumber)) {
                    Toast.makeText(context, "Nhập vào số cổng hợp lệ...", Toast.LENGTH_SHORT).show();
                    return;
                }
                webView.setVisibility(View.VISIBLE);
                webView.setWebViewClient(new MyClient());
                webView.loadUrl("http://" + ipAddress + ":" + portNumber);
            }
        });

    }

    private class MyClient extends WebViewClient {
        @Override
        public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
            view.loadUrl(request.getUrl().toString());
            return true;
        }
    }
}
