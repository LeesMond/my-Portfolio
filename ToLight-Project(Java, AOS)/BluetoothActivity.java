package com.example.tolight;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.view.View;
import android.widget.Button;

import java.util.Locale;

public class BluetoothActivity extends AppCompatActivity {
    public TextToSpeech tts;
    Button button3;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.bluetooth);
        tts = new TextToSpeech(BluetoothActivity.this, status -> {
            if(status != TextToSpeech.ERROR){
                tts.setLanguage(Locale.KOREAN);
            }
            tts.speak("블루투스 연결 페이지 입니다." +
                            "원하지 않으시면 스마트폰 아래쪽 영역을 터치해주세요",
                    TextToSpeech.QUEUE_FLUSH, null);
        });
        button3 = findViewById(R.id.button3);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                tts.speak("메인화면으로 돌아갑니다. 시각장애인용 장애물 안내프로그램 입니다." +
                        "시작 하시려면 스마트폰의 가운데 영역을 터치해 주세요."+
                        "블루투스 연결을 하시려면 스마트폰의 상단을 터치해 주세요", TextToSpeech.QUEUE_FLUSH,
                        null);
                finish();
            }
        });
    }
}