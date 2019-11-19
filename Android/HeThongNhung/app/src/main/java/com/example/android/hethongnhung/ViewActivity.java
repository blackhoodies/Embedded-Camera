package com.example.android.hethongnhung;

import android.os.Bundle;
import android.util.Log;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.android.hethongnhung.Controller.StoreData;

import org.json.JSONObject;

public class ViewActivity extends AppCompatActivity {
    private final String TAG = ViewActivity.class.getName();
    private String ipAddress;
    private int port;
    private WebView webView;

    @Override
    protected void onStop() {
        super.onStop();
        finish();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        finish();
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_view);

        JSONObject dataPacket;
        try{
            dataPacket = StoreData.loadData(ViewActivity.this);
            ipAddress = dataPacket.getString("address");
            port = dataPacket.getInt("port");
        } catch (Exception e){
            Log.e(TAG, "Loi JSONObject. Thiet lap thong so mac dinh");
            ipAddress = "www.google.com";
            port = 80;
        }
        Log.i("ViewActivity", String.format("address: %s, port: %d", ipAddress, port));

        webView = (WebView) findViewById(R.id.webview_view);
        webView.setWebViewClient(new MyClient());
        webView.loadUrl("http://" + ipAddress + ":" + port);
    }

    private class MyClient extends WebViewClient {
        @Override
        public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
            view.loadUrl(request.getUrl().toString());
            return true;
        }
    }


}
