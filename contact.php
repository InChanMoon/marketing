<?php $page_title = '문의하기'; include 'includes/header.php'; ?>

    <!-- Page Header -->
    <section class="hero" style="min-height: 400px; padding: 150px 0 100px;">
        <div class="hero-content">
            <h1>무료 상담 신청</h1>
            <p>지금 바로 문의하시면 업종별 맞춤 마케팅 전략을 제안해드립니다</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact">
        <div class="container">
            <div class="contact-container">
                <!-- Contact Info -->
                <div class="contact-info">
                    <h3>연락처 정보</h3>

                    <div class="contact-item">
                        <div class="contact-icon">💬</div>
                        <div class="contact-item-content">
                            <h4>카카오톡 ID</h4>
                            <p>pres00</p>
                        </div>
                    </div>

                    <div class="contact-item">
                        <div class="contact-icon">📞</div>
                        <div class="contact-item-content">
                            <h4>전화 문의</h4>
                            <p>010-3966-7687</p>
                        </div>
                    </div>

                    <div class="contact-item">
                        <div class="contact-icon">⏰</div>
                        <div class="contact-item-content">
                            <h4>상담 시간</h4>
                            <p>평일 09:00 - 18:00</p>
                        </div>
                    </div>

                    <div class="contact-item">
                        <div class="contact-icon">✉️</div>
                        <div class="contact-item-content">
                            <h4>빠른 응답</h4>
                            <p>카카오톡 상담 추천</p>
                        </div>
                    </div>

                    <div style="margin-top: 2rem; border-radius: 10px; overflow: hidden;">
                        <!-- 이미지: 상담 안내 (권장 크기: 600x400px) -->
                        <img src="images/contact-consultation.jpg" alt="전문 상담사가 고객과 상담하는 모습, 친절하고 전문적인 분위기, 600x400px" style="width: 100%; height: auto; display: block;">
                    </div>
                </div>

                <!-- Contact Form -->
                <div class="contact-form">
                    <h3 style="margin-bottom: 2rem;">문의 양식</h3>
                    <form action="contact_process.php" method="POST" id="contactForm">
                        <div class="form-group">
                            <label for="name">이름 *</label>
                            <input type="text" id="name" name="name" required placeholder="이름을 입력하세요">
                        </div>

                        <div class="form-group">
                            <label for="phone">연락처 *</label>
                            <input type="tel" id="phone" name="phone" required placeholder="010-0000-0000">
                        </div>

                        <div class="form-group">
                            <label for="industry">업종 *</label>
                            <select id="industry" name="industry" required>
                                <option value="">업종을 선택하세요</option>
                                <option value="법률">법률</option>
                                <option value="병의원">병의원</option>
                                <option value="왁싱/뷰티">왁싱/뷰티</option>
                                <option value="청소/방역">청소/방역</option>
                                <option value="누수/방수">누수/방수</option>
                                <option value="마케팅">마케팅</option>
                                <option value="학원/교육">학원/교육</option>
                                <option value="요식업">요식업</option>
                                <option value="인테리어">인테리어</option>
                                <option value="자동차">자동차</option>
                                <option value="금융/보험">금융/보험</option>
                                <option value="부동산">부동산</option>
                                <option value="기타">기타</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="keywords">희망 키워드</label>
                            <input type="text" id="keywords" name="keywords" placeholder="예: 강남 피부과, 서울 인테리어">
                        </div>

                        <div class="form-group">
                            <label for="message">문의 내용 *</label>
                            <textarea id="message" name="message" required placeholder="문의하실 내용을 자세히 작성해주세요"></textarea>
                        </div>

                        <button type="submit" class="btn btn-gradient" style="width: 100%;">
                            무료 상담 신청하기
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Additional Info -->
    <section class="services">
        <div class="container">
            <div class="section-title">
                <h2>상담 후 진행 프로세스</h2>
                <p>체계적인 프로세스로 최상의 결과를 만들어냅니다</p>
            </div>

            <div class="services-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
                <div class="service-card">
                    <div class="service-content">
                        <h3 style="font-size: 2rem; color: var(--primary-color);">1</h3>
                        <h4>무료 상담</h4>
                        <p>업종과 목표를 파악하고 맞춤 전략을 제안합니다</p>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-content">
                        <h3 style="font-size: 2rem; color: var(--primary-color);">2</h3>
                        <h4>키워드 분석</h4>
                        <p>데이터 기반의 키워드 리서치를 진행합니다</p>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-content">
                        <h3 style="font-size: 2rem; color: var(--primary-color);">3</h3>
                        <h4>계약 및 착수</h4>
                        <p>명확한 계약 후 즉시 작업을 시작합니다</p>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-content">
                        <h3 style="font-size: 2rem; color: var(--primary-color);">4</h3>
                        <h4>콘텐츠 제작</h4>
                        <p>전문 작가진이 고품질 콘텐츠를 제작합니다</p>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-content">
                        <h3 style="font-size: 2rem; color: var(--primary-color);">5</h3>
                        <h4>블로그 배포</h4>
                        <p>최적화된 블로그에 전략적으로 배포합니다</p>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-content">
                        <h3 style="font-size: 2rem; color: var(--primary-color);">6</h3>
                        <h4>성과 리포트</h4>
                        <p>실시간 모니터링과 상세 리포트를 제공합니다</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

<?php include 'includes/footer.php'; ?>
