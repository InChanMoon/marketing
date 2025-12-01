<?php
// ========================================
// Prestige Marketing - Contact Form Handler
// ========================================

// Set response header to JSON
header('Content-Type: application/json; charset=utf-8');

// Security: Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode([
        'success' => false,
        'message' => 'Method not allowed'
    ]);
    exit;
}

// Get form data
$name = isset($_POST['name']) ? trim($_POST['name']) : '';
$phone = isset($_POST['phone']) ? trim($_POST['phone']) : '';
$industry = isset($_POST['industry']) ? trim($_POST['industry']) : '';
$keywords = isset($_POST['keywords']) ? trim($_POST['keywords']) : '';
$message = isset($_POST['message']) ? trim($_POST['message']) : '';

// Validation
$errors = [];

if (empty($name)) {
    $errors[] = '이름을 입력해주세요.';
}

if (empty($phone)) {
    $errors[] = '연락처를 입력해주세요.';
} elseif (!preg_match('/^01[0-9]-?[0-9]{3,4}-?[0-9]{4}$/', $phone)) {
    $errors[] = '올바른 연락처 형식이 아닙니다.';
}

if (empty($industry)) {
    $errors[] = '업종을 선택해주세요.';
}

if (empty($message)) {
    $errors[] = '문의 내용을 입력해주세요.';
}

// If there are validation errors
if (!empty($errors)) {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'message' => implode(' ', $errors),
        'errors' => $errors
    ]);
    exit;
}

// Sanitize input
$name = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
$phone = htmlspecialchars($phone, ENT_QUOTES, 'UTF-8');
$industry = htmlspecialchars($industry, ENT_QUOTES, 'UTF-8');
$keywords = htmlspecialchars($keywords, ENT_QUOTES, 'UTF-8');
$message = htmlspecialchars($message, ENT_QUOTES, 'UTF-8');

// Get client IP and timestamp
$ip_address = $_SERVER['REMOTE_ADDR'];
$timestamp = date('Y-m-d H:i:s');
$date_formatted = date('Ymd_His');

// Create inquiries directory if it doesn't exist
$inquiries_dir = __DIR__ . '/inquiries';
if (!file_exists($inquiries_dir)) {
    mkdir($inquiries_dir, 0755, true);
}

// Save to file (CSV format)
$csv_file = $inquiries_dir . '/inquiries.csv';
$file_exists = file_exists($csv_file);

$csv_data = [
    $timestamp,
    $name,
    $phone,
    $industry,
    $keywords,
    $message,
    $ip_address
];

$fp = fopen($csv_file, 'a');
if ($fp) {
    // Write header if file is new
    if (!$file_exists) {
        fputcsv($fp, ['날짜/시간', '이름', '연락처', '업종', '희망키워드', '문의내용', 'IP주소']);
    }

    fputcsv($fp, $csv_data);
    fclose($fp);
}

// Save to individual text file for easy reading
$txt_file = $inquiries_dir . '/inquiry_' . $date_formatted . '_' . uniqid() . '.txt';
$txt_content = "=============================================\n";
$txt_content .= "Prestige Marketing 문의 접수\n";
$txt_content .= "=============================================\n\n";
$txt_content .= "접수 일시: {$timestamp}\n";
$txt_content .= "이름: {$name}\n";
$txt_content .= "연락처: {$phone}\n";
$txt_content .= "업종: {$industry}\n";
$txt_content .= "희망 키워드: " . ($keywords ? $keywords : '(입력 안함)') . "\n";
$txt_content .= "IP 주소: {$ip_address}\n\n";
$txt_content .= "문의 내용:\n";
$txt_content .= "---------------------------------------------\n";
$txt_content .= $message . "\n";
$txt_content .= "---------------------------------------------\n";

file_put_contents($txt_file, $txt_content);

// Optional: Send email notification
// Uncomment and configure the following section to enable email notifications

/*
$to = "your-email@example.com"; // 받는 사람 이메일 주소
$subject = "[Prestige Marketing] 새로운 문의: " . $name;
$email_message = "
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background: #1e40af; color: white; padding: 20px; text-align: center; }
        .content { background: #f8fafc; padding: 20px; }
        .field { margin-bottom: 15px; }
        .label { font-weight: bold; color: #1e40af; }
        .value { margin-left: 10px; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h2>새로운 문의가 접수되었습니다</h2>
        </div>
        <div class='content'>
            <div class='field'>
                <span class='label'>접수 일시:</span>
                <span class='value'>{$timestamp}</span>
            </div>
            <div class='field'>
                <span class='label'>이름:</span>
                <span class='value'>{$name}</span>
            </div>
            <div class='field'>
                <span class='label'>연락처:</span>
                <span class='value'>{$phone}</span>
            </div>
            <div class='field'>
                <span class='label'>업종:</span>
                <span class='value'>{$industry}</span>
            </div>
            <div class='field'>
                <span class='label'>희망 키워드:</span>
                <span class='value'>{$keywords}</span>
            </div>
            <div class='field'>
                <span class='label'>문의 내용:</span>
                <div style='background: white; padding: 15px; margin-top: 10px; border-left: 4px solid #1e40af;'>
                    " . nl2br($message) . "
                </div>
            </div>
            <div class='field'>
                <span class='label'>IP 주소:</span>
                <span class='value'>{$ip_address}</span>
            </div>
        </div>
    </div>
</body>
</html>
";

$headers = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: Prestige Marketing <noreply@prestigemarketing.com>\r\n";

mail($to, $subject, $email_message, $headers);
*/

// Return success response
echo json_encode([
    'success' => true,
    'message' => '문의가 성공적으로 접수되었습니다.',
    'data' => [
        'timestamp' => $timestamp,
        'name' => $name,
        'industry' => $industry
    ]
]);

exit;
?>
