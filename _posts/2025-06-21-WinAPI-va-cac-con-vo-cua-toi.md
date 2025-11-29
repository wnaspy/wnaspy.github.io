---
layout: post
title: "WinAPI for hacker"
categories: Pentest
tags: [beginner, pentest, redteam, PE, coding, tutorial, beginner]
---

# Thực hành và kiến thức
```
#include "Windows.h"

int WINAPI WinMain(HINSTANCE hInstance, // windows instance handler
	HINSTANCE hPreInstance,  // not to use in Win32
	LPSTR lpCmdLine, // need to run Windows mode in commandline mode
	int nCmdShow // Windows display mode
	)
{
	MessageBoxA(NULL, "Tbao", "tbao", MB_OK);
	return NULL;
}
```
- Hãy bắt đầu bằng một đoạn code cơ bản, 
+ dòng 1 là sẽ include thư viện Windows.h chứa các hàm của WinAPI
+ Dòng 3-6 sẽ mô tả hàm int WINAPI WinMain() với các tham số.
+ Dòng 9 sẽ gọi hàm MessageBox()
# Các kiểu dữ liệu
1. Dữ liệu cơ bản
- **BOOL**: Gôm 0 và 1, sẽ tốt hơn khi dùng 0 thay cho NULL
- **BYTE**: gồm 8 bit
- **DWORD**: 32 bit unsigned integer
- **INT**: 32 bit integer
- **LONG**: 32 bit integer
- **NULL**: null pointer - cách dùng `void *NULL = 0;`
- **UINT**: 32 bit unsigned integer

unsigned là khai báo số ko âm

2. Decriptor cho kiểu dữ liệu
- **HANDLE**: decriptor of object
- **HBITMAP**: decriptor of bitmap. From the name of handle bitmap.
- **HCURSOR** – descriptor of cursor. From the name of handle cursor.
- **HDC** – descriptor of device context. From the name of handle device context.
- **HFONT** – descriptor of font. From the name of handle font.
- **HICONS** – descriptor of icons. From the name of handle icons.
- **HINSTANCE** – descriptor of the application instance. From the name of handle instance.
- **HMENU** – descriptor of menu. From the name of handle menu.
- **HPEN** – descriptor of pen. From the name of handle pen.
- **HWND** – descriptor of window. From the name of handle window.
3. Kiểu string
- Trong WINAPI ta sẽ có 2 loại encoding cần lưu ý: 1 là ANSI (1 byte kí tự) và 2 là UNICODE (2 bytes kí tự)
ví dụ ANSI
`char str[10];`
ví dụ UNICODE
`wchar_t str[10];`
- **LPCSTR** – a pointer to a constant string, ending with zero-interrupter. From the name of long pointer constant string.
- **LPCTSTR** – a pointer to a constant string, without UNICODE. From the name of long pointer constant TCHAR string. This add-in function to LPCSTR.
- **LPCWSTR** – a pointer to a constant UNICODE string. From the name of long pointer constant wide character string. This add-in function to LPCSTR.
- **LPSTR** – a pointer to a string, ending with zero-interrupter. From the name of long pointer string.
- **LPTSTR** – a pointer to a string without UNICODE. From the name of long pointer TCHAR string. This add-in function to LPSTR.
- **LPWSTR** – a pointer to a UNICODE string. From the name of long pointer wide character string. This add-in function to LPSTR.
- **TCHAR** – symbol data type — same as char and wchar_t.
4. Utility data types
- LPARAM – type to describe lParam (long parameter). Used with wparam in some functions.
- LRESULT – value, returned by the window procedure has long data type.
- WPARAM – type to describe wParam (word parameter). Used with lParam in some functions.

# Tạo thủ tục WIndows hoàn chỉnh bằng WinAPI
- tạo 2 hàm, 1 hàm là WinMain với các tham số lấy từ ví dụ trên, hàm thứ 2 là xử lý các tiến trình (vd: WndProc())
- tạo mổ tả của windows hMainWnd và đăng kí windows class WNDCLASSEX, phải nằm trong WinMain
- Tạo khuôn cho windows, nằm trong WinMain
- Viết chu trình xử lý message, nằm trong WndProc
- Tạo hàm hiển thị Windows


```
#include "Windows.h"

int WINAPI WinMain(HINSTANCE hInstance,
	HINSTANCE hPreInstance,
	LPSTR lpCmdLine, // need to run Windows mode in commandline mode
	int nCmdShow // Windows display mode
	)
{
	int result = MessageBoxA(NULL, "Do you love me!!?", "love", MB_ICONQUESTION | MB_YESNO);
	switch (result)
	{
	case IDYES:
		MessageBoxA(NULL, "Yeah, i love yuu too!!", "love", MB_OK | MB_ICONASTERISK); break;
	case IDNO:
		MessageBoxA(NULL, "OKay, but i love u, just wanna say that", "sad", MB_OK | MB_ICONSTOP); break;
	}
	return 0;
}
```

```
#include <windows.h>

TCHAR mainMessage[] = L"Hacked by Spycio.Kon";

LRESULT CALLBACK WndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    HDC hdc;
    PAINTSTRUCT ps;
    RECT rect;
    COLORREF colorText = RGB(255, 0, 0); 

    switch (uMsg)
    {
    case WM_PAINT:
        hdc = BeginPaint(hWnd, &ps);
        GetClientRect(hWnd, &rect);
        SetTextColor(hdc, colorText);
        SetBkMode(hdc, TRANSPARENT); 
        DrawText(hdc, mainMessage, -1, &rect, DT_SINGLELINE | DT_CENTER | DT_VCENTER);
        EndPaint(hWnd, &ps);
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, uMsg, wParam, lParam);
    }

    return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
    LPSTR lpCmdLine, int nCmdShow)
{
    const wchar_t CLASS_NAME[] = L"MyWindowClass";

    WNDCLASS wc = { };
    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);

    RegisterClass(&wc);

    HWND hWnd = CreateWindowEx(
        0,
        CLASS_NAME,
        L"Window Title",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 400, 200,
        NULL, NULL, hInstance, NULL
    );

    if (hWnd == NULL)
        return 0;

    ShowWindow(hWnd, nCmdShow);
    UpdateWindow(hWnd);

    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

```
{% include embed/youtube.html id="KvM9R5IMOOs" %}
