package com.example.tolight;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.widget.Button;

import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    public TextToSpeech tts;
    Button button1;
    Button button2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tts = new TextToSpeech(MainActivity.this, status -> {
            if(status != TextToSpeech.ERROR){
                tts.setLanguage(Locale.KOREAN);
            }
            tts.speak("시각장애인용 장애물 안내프로그램 입니다. " +
                            "시작 하시려면 스마트폰의 가운데 영역을 터치해 주세요."+
                            "블루투스 연결을 하시려면 스마트폰의 상단을 터치해 주세요",
                    TextToSpeech.QUEUE_FLUSH, null);
        });
        button1 = findViewById(R.id.button1);
        button1.setOnClickListener(view -> {
            tts.speak("블루투스 연결",
                    TextToSpeech.QUEUE_FLUSH, null);
            Intent intent = new Intent(getApplicationContext(),BluetoothActivity.class);
            startActivity(intent);
        });
        button2 = findViewById(R.id.button2);
        button2.setOnClickListener(view -> tts.speak("어플리케이션을 실행 하겠습니다",
                TextToSpeech.QUEUE_FLUSH, null));
    }
}