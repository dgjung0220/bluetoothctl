package com.hmc.adkit;

public class DataFormatDTO {

    private String datetime;
    private String text;

    public DataFormatDTO() { }

    public DataFormatDTO(String datetime, String text) {
        this.datetime = datetime;
        this.text = text;
    }
    public String getDatetime() {
        return datetime;
    }
    public void setDatetime(String datetime) {
        this.datetime = datetime;
    }
    public String getText() {
        return text;
    }
    public void setText(String text) {
        this.text = text;
    }
}
